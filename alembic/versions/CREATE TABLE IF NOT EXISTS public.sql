CREATE TABLE IF NOT EXISTS public.users
(
    id integer NOT NULL DEFAULT nextval('users_id_seq'::regclass),
    api_keys character varying COLLATE pg_catalog."default" NOT NULL,
    name character varying COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT users_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE public.users
    OWNER to muna;

-- Index: public.ix_users_api_keys
CREATE UNIQUE INDEX IF NOT EXISTS ix_users_api_keys
    ON public.users USING btree
    (api_keys COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;
-- Index: public.ix_users_name
CREATE INDEX IF NOT EXISTS ix_users_name
    ON public.users USING btree
    (name COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;
SELECT * FROM users;    