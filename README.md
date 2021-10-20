# دیتاست استان‌ها، شهرستان‌ها، بخش‌ها، دهستان‌ها و شهر-یا-روستاهای ایران

## How to use

- Create a table with the following DDL.

```
create table %TABLE_NAME%
(
    id     mediumint auto_increment
        primary key,
    title  varchar(200) charset utf8mb4                                        not null,
    type   enum ('ostan', 'shahrestan', 'bakhsh', 'dehestan', 'shahr_roosta')  not null,
    parent int unsigned                                                        null
)
    collate = utf8mb4_persian_ci;

create index _type_asc_index
    on %TABLE_NAME% (type);
```

- Clone this repo and enter it.
```
git clone https://github.com/kmirzavaziri/iranCitiesDataset.git
cd iranCitiesDataset
```

- Make the `.sql` file with the following script.

```
python3 make.py %TABLE%
```

- Import the `.sql` into the database. (Beware that the sql file `TRUNCATE`s the table and then inserts the rows.)

```
nohup mysql %CREDENTIALS% %DATABASE% < iranAdministrativeDivision.sql
```