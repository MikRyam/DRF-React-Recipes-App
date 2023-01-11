import React from 'react';
import {Link} from "react-router-dom";
import CategoryItem from "./CategoryItem";
import {useGetCategoriesQuery} from "../redux/recipes.api";

const Header = () => {
  const { data: categories, error, isLoading } = useGetCategoriesQuery();

  if (isLoading) return <h1>Loading...</h1>

  return (
    <header>
      {/*<img src={reactLogo} className="nav--icon" alt="React logo" />*/}
      <Link to="/"><h3 className='nav--logo_text'>РЕЦЕПТЫ</h3></Link>
      <div className="navLinks">
        {error ? (
            <>Oh no, there was an error</>
          ) :
          categories?.map(({id, name, slug}) => <CategoryItem key={id} name={name} slug={slug} id={id}/>)
        }
      </div>

    </header>
  );
};

export default Header;
