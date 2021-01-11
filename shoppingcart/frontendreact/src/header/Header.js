import React from "react";
import "././Header.css";
import { Link } from "react-router-dom";
import SearchIcon from "@material-ui/icons/Search";
import ShoppingCartIcon from "@material-ui/icons/ShoppingCart";
import { useStateValue } from "../services/StateProvider";
import { auth } from "../services/firebase";
// import Icon from '@material-ui/core/Icon'; //
// import { green } from '@material-ui/core/colors';

function Header() {
  const [{ basket, user }] = useStateValue();

  const login = () => {
    if(user){
      auth.signOut();
    }
  };

  //This is for to make responsive
  // const openNav = () => {
  //   document.getElementById("mySidenav").style.width = "250px";
  // };
  
  // const closeNav = () => {
  //   document.getElementById("mySidenav").style.width = "0";
  // };

  return (
    
    <nav className="header">

      <div className="header__first_main_res">
      <div className="header__first">
        
        <input type="checkbox" className="check"/>
        <label for="check" className="checkbtn" >
        {/* <Icon className="fas fa-bars"  className="checkbtnIcon" /> */}
        {/* <Icon className="fa fa-plus-circle" style={{ color: green[500] }} /> */}
        <i className="fas fa-bars" ></i>
        </label>

      <Link to="/">
        <img
          src="data:image/jpeg;base64,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"
          className="header_logo"
          alt="logo"
        />
      </Link>
      </div>

      <div className="header__second__right">
      
          <Link to={!user && "/login"} className="header__link">
              <div onClick={login} className="header__option">
                <span className="header__optionLineOne"> {user?.email}</span>
                <span className="header__optionLineTwo"> {user ? 'Sign Out' : 'Sign In'}</span>
              </div>
            </Link>
            
            <Link to="/checkout" className="header__link">
          <ShoppingCartIcon />

          <span className="header__optionLineTwo header__basketCount">
                  {basket?.length}
                </span>
                </Link>
      </div>
      </div>

      

      <div className="header__search">
        <input type="text" className="header__searchInput" value="" placeholder="Search " />

        <SearchIcon className="header__searchIcon" />
      </div>

      <div className="header__nav">
        <Link to={!user && "/login"} className="header__link">
          <div onClick={login} className="header__option">
            <span className="header__optionLineOne">Hello, {user?.email}</span>
            <span className="header__optionLineTwo"> {user ? 'Sign Out' : 'Sign In'}</span>
          </div>
        </Link>

        <Link to="/" className="header__link">
          <div className="header__option">
            <span className="header__optionLineOne">Returns</span>
            <span className="header__optionLineTwo">& Orders</span>
          </div>
        </Link>

        <Link to="/" className="header__link">
          <div className="header__option">
            <span className="header__optionLineOne"></span>
            <span className="header__optionLineTwo"></span>
          </div>
        </Link>

        <Link to="/checkout" className="header__link">
          <div className="header__optionBasket">
            <ShoppingCartIcon />

            <span className="header__optionLineTwo header__basketCount">
              {basket?.length}
            </span>
          </div>
        </Link>
      </div>
      
     

    </nav>

      
  );
}

export default Header;
