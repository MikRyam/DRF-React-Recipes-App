import React from 'react';
import {Link} from "react-router-dom";

const RecipeItem = ({catId, recipe}) => {
  return (
    <Link to={`/recipes/${catId}/${recipe.slug}`}>
      <p className='menuLink'>{recipe.title}</p>
    </Link>
  );
};

export default RecipeItem;
