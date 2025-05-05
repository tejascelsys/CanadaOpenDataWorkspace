CREATE   PROCEDURE MoveTablesToNewSchema
    @OldSchema NVARCHAR(128), -- Name of the existing schema
    @NewSchema NVARCHAR(128) -- Name of the new schema
AS
BEGIN
    BEGIN TRY
        -- Start the transaction
        BEGIN TRANSACTION;

        -- Create the new schema if it does not exist
        IF NOT EXISTS (
            SELECT 1
            FROM sys.schemas
            WHERE name = @NewSchema
        )
        BEGIN
            DECLARE @CreateSchemaSQL NVARCHAR(MAX);
            SET @CreateSchemaSQL = N'CREATE SCHEMA ' + QUOTENAME(@NewSchema);
            EXEC sp_executesql @CreateSchemaSQL;
        END;

        -- Generate and execute SQL to move all tables from the old schema to the new schema
        DECLARE @MoveSQL NVARCHAR(MAX);

        SELECT @MoveSQL = STRING_AGG(
            N'ALTER SCHEMA ' + QUOTENAME(@NewSchema) +
            N' TRANSFER ' + QUOTENAME(@OldSchema) + N'.' + QUOTENAME(TABLE_NAME),
            N'; '
        )
        FROM INFORMATION_SCHEMA.TABLES
        WHERE TABLE_SCHEMA = @OldSchema AND TABLE_TYPE = 'BASE TABLE';

        -- Execute the combined SQL to transfer all tables
        IF @MoveSQL IS NOT NULL
        BEGIN
            EXEC sp_executesql @MoveSQL;
        END

        -- Commit the transaction
        COMMIT TRANSACTION;
    END TRY
    BEGIN CATCH
        -- Rollback the transaction in case of an error
        ROLLBACK TRANSACTION;

        -- Rethrow the error
        THROW;
    END CATCH;
END;