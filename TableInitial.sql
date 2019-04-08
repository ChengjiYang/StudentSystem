use StudentSystem;
create table class(
  id int,
  title char(255)
);

create table student(
  id int,
  name char(255),
  classID int
);

create table teacher(
  id int,
  name char(255)
);

create table teacher2class(
  id int,
  teacherid int,
  classid int
);

insert into class values (1, "class1"), (2, "class2");

insert into teacher value (1, "Lin1"), (2, "Lin2"), (3, "Yuan");