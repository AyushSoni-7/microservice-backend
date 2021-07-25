FROM postgres:alpine
ADD scripts/10_category.sql /docker-entrypoint-initdb.d
RUN chmod a+r /docker-entrypoint-initdb.d/*

