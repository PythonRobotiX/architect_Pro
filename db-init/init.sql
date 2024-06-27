DO
$$
BEGIN
   IF NOT EXISTS (
      SELECT 
      FROM   pg_catalog.pg_roles 
      WHERE  rolname = 'admin_db') THEN

      CREATE ROLE admin_db WITH LOGIN PASSWORD 'Gab5i9A6k8Ry';
   END IF;
END
$$;

DO
$$
BEGIN
   IF NOT EXISTS (
      SELECT 
      FROM   pg_database 
      WHERE  datname = 'arya_web_db') THEN

      CREATE DATABASE arya_web_db;
   END IF;
END
$$;

GRANT ALL PRIVILEGES ON DATABASE arya_web_db TO admin_db;
