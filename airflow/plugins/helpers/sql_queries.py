class SqlQueries:

    reviews_table_insert = ("""
        SELECT 	reviews.ReviewId,
                recipes.RecipeId,
                reviews.AuthorId,
                reviews.Rating,
                reviews.Review,
                reviews.DateSubmitted
        FROM    staging_reviews reviews, 
                staging_recipes recipes
        WHERE   reviews.RecipeId = recipes.RecipeId and
                Rating is not null and
                ReviewId is not null
    """)
    
    author_table_insert = ("""
        SELECT 	distinct AuthorId,
                AuthorName
        FROM    staging_reviews
        WHERE   AuthorId is not null
    """)

    category_table_insert = ("""
        SELECT  distinct RecipeCategory
        FROM    staging_recipes
        WHERE   RecipeCategory is not null
    """)

    recipes_table_insert = ("""
        SELECT 	distinct RecipeId,
                Name,
                CookTime,
                PrepTime,
                TotalTime,
                Description,
                Images,
                category.RecipeCategoryId,
                Keywords,
                AggregatedRating,
                ReviewCount,
                Calories,
                RecipeServings,
                RecipeYield,
                RecipeInstructions
        FROM    staging_recipes recipes, 
                category category
        WHERE   recipes.RecipeCategory = category.RecipeCategory and
                RecipeId is not null and
                Name is not null
    """)

    time_table_insert = ("""
        SELECT distinct DateSubmittedId, 
               extract(hour from DateSubmittedId), 
               extract(day from DateSubmittedId), 
               extract(month from DateSubmittedId), 
               extract(year from DateSubmittedId) 
        FROM   reviews
        WHERE  DateSubmittedId is not null
    """)