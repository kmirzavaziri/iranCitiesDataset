# دیتاست استان‌ها، شهرستان‌ها، بخش‌ها، دهستان‌ها و آبادی‌های ایران

## Table DDL
```
create table Dataset_IranAdministrativeDivision
(
    id     mediumint auto_increment
        primary key,
    title  varchar(200) charset utf8mb4                                        not null,
    type   enum ('ostan', 'shahrestan', 'bakhsh', 'dehestan', 'shahrorroosta') not null,
    parent int unsigned                                                        null
)
    collate = utf8mb4_persian_ci;

create index _type_asc_index
    on Dataset_IranAdministrativeDivision (type);

```