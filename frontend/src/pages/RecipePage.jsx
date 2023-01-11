import React from 'react';
import {useParams} from "react-router-dom";
import {useGetRecipeQuery} from "../redux/recipes.api";
import ButtonGoBack from "../components/ButtonGoBack";

const RecipePage = () => {
  const {slug} = useParams();
  const {data: recipe, error, isLoading} = useGetRecipeQuery(slug);
  const ingredients = recipe?.ingredients.split('-');
  const instructions = recipe?.instructions.split('-');

  if (isLoading) return (
    <div className="container">
      <h1 className="mainTitle">Loading...</h1>
    </div>
  )

  return (
    <>
      <ButtonGoBack />
      {error ? (
          <>Oh no, there was an error</>
        ) :
        (
          <div className="recipeCard">
            <h2>{recipe?.title}</h2>
            <div>
              <h4>Ингредиенты:</h4>
              <ul>
                {
                  ingredients?.map((ingredient, index) => <li key={index + 1}
                                                              className='cardTextIngredients'>{ingredient}</li>)
                }
              </ul>
              <h4>Инструкция:</h4>
              <ol>
                {
                  instructions?.map((instruction, index) => <li key={index + 1}
                                                                className='cardTextInstructions'>{instruction}</li>)
                }
              </ol>
            </div>
          </div>
        )
      }
    </>
  );
};

export default RecipePage;
