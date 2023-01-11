import React from 'react';
import {useGetCategoriesQuery} from "../redux/recipes.api";
import CategoryItem from "../components/CategoryItem";

const HomePage = () => {
  const { data: categories, error, isLoading } = useGetCategoriesQuery()

  if (isLoading) return (
    <div className="container">
      <h1 className="mainTitle">Loading...</h1>
    </div>
  )

  return (
    <div className="container">
      <h1 className="mainTitle">РЕЦЕПТЫ</h1>
      <div className="mainPageLinks">
        {error ? (
            <>Oh no, there was an error</>
          ) :
          categories?.map(({id, name}) => <CategoryItem key={id} name={name} id={id}/>)
        }
      </div>

    </div>
  );
};

export default HomePage;
