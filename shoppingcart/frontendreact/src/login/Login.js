import React, { useState } from "react";
import { Link, useHistory } from "react-router-dom";
import "../login/Login.css";
import { auth } from "../services/firebase";


function Login() {
  const history = useHistory();

  const[email, setEmail] = useState('');
  const[password, setPassword] = useState('');

  const login = (event) => {
    event.preventDefault(); //this stops referss
    //do the login logic.....

    auth.signInWithEmailAndPassword(email, password).then((auth) => {
      // logged in , redirect to home page
      history.push("/");
    }).catch(
      (e) => alert(e.message)

    );
  };

  const register = (event) => {
    event.preventDefault(); //this stops referss
    //do the login logic...
    auth.createUserWithEmailAndPassword(email, password)
    .then((auth) => {
      //created a user and logged in
      history.push("/"); 
    })
    .catch((e) => alert(e.message));
  };

  return (
    <div className="login">
      <Link to="/">
        <img
          className="login__logo"
          src="data:image/png;base64,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"
          alt=""
        />
      </Link>

      <div className="login__container">
        <h1>Sign in</h1>

        <form>
          <h5>E-mail</h5>
          <input type="email" name="" value={email} onChange={event => setEmail(event.target.value)} />
          <h5>Password</h5>
          <input type="password" name="" value={password} onChange={event => setPassword(event.target.value)} />
          <button onClick={login} className="login__signInButton" type="submit">
            Sign In
          </button>
        </form>

        <p>
          By Signing-in you agree to shopping conditions of Use & Sale. Please
          see our Privacy Notice, Our Cookies Notice and our interest-Based Ads
          Notice.
        </p>

        <button onClick={register} className="login__registerButton">
          Create your Shopping Account
        </button>
      </div>
    </div>
  );
}

export default Login;
