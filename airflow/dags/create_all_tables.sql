CREATE TABLE IF NOT EXISTS staging_reviews (
	ReviewId int,
	RecipeId int,
	AuthorId int,
	AuthorName varchar(256),
	Rating int,
	Review varchar(65535),
	DateSubmitted timestamptz,
	DateModified timestamptz
);

CREATE TABLE IF NOT EXISTS staging_recipes (
	RecipeId int,
	Name varchar(256),
	AuthorId int,
	AuthorName varchar(256),
	CookTime varchar(256),
	PrepTime varchar(256),
	TotalTime varchar(256),
	DatePublished timestamptz,
	Description varchar(65535),
	Images varchar(65535),
	RecipeCategory varchar(256),
	Keywords varchar(4000),
	RecipeIngredientQuantities varchar(65535),
	RecipeIngredientParts varchar(65535),
	AggregatedRating varchar(256),
	ReviewCount varchar(256),
	Calories varchar(256),
	FatContent varchar(256),
	SaturatedFatContent varchar(256),
	CholesterolContent varchar(256),
	SodiumContent varchar(256),
	CarbohydrateContent varchar(256),
	FiberContent varchar(256),
	SugarContent varchar(256),
	ProteinContent varchar(256),
	RecipeServings varchar(4000),
	RecipeYield varchar(4000),
	RecipeInstructions varchar(65535)
);

CREATE TABLE IF NOT EXISTS reviews (
	ReviewId int,
	RecipeId int,
	AuthorId int,
	Rating int,
	Review varchar(65535),
	DateSubmittedId timestamptz,
	CONSTRAINT reviews_pkey PRIMARY KEY (ReviewId)
);

CREATE TABLE IF NOT EXISTS recipes (
	RecipeId int,
	Name varchar(256),
	CookTime varchar(256),
	PrepTime varchar(256),
	TotalTime varchar(256),
	Description varchar(65535),
	Images varchar(65535),
	RecipeCategoryId int,
	Keywords varchar(4000),
	AggregatedRating varchar(256),
	ReviewCount varchar(256),
	Calories varchar(256),
	RecipeServings varchar(4000),
	RecipeYield varchar(4000),
	RecipeInstructions varchar(65535),
    CONSTRAINT recipes_pkey PRIMARY KEY (RecipeId)
);

CREATE TABLE IF NOT EXISTS category (
	RecipeCategoryId INT IDENTITY(1, 1),
	RecipeCategory varchar(256),
	CONSTRAINT category_pkey PRIMARY KEY (RecipeCategoryId)
);

CREATE TABLE IF NOT EXISTS time (
	DateSubmittedId timestamptz,
	hour int,
	day int,
	month int,
	year int,
	CONSTRAINT time_pkey PRIMARY KEY (DateSubmittedId)
) ;

CREATE TABLE IF NOT EXISTS author (
	AuthorId int,
	AuthorName varchar(256),
	CONSTRAINT author_pkey PRIMARY KEY (AuthorId)
);