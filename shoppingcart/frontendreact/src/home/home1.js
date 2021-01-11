import axios from 'axios';
import {Link} from 'react-router-dom'
import React, { Component } from 'react'
import CartIcon from "./svg/shopping-cart-solid.svg";
import {DataContext} from './Context'


class Home extends React.Component {

    state = {
        details: [],
    }

    componentDidMount() {

        let data;

        axios.get('http://http://127.0.0.1:8000/api/orders/')
            .then(res => {
                data = res.data;
                this.setState({
                    details: data
                });
            })
            .catch(err => {
            })
    }

    render() {
       
        return (

            <div id="product">

                {this.state.details.map((detail, id) => (

                             <div className="card" key={detail.id}>
                           {/*      <Link to={detail.Title}>*/}
                           {/*    <img src={product.src} alt=""/>*/}
                           {/</Link>/}
                            <div>
                                <div>
                                    <h1>{detail.Title} </h1>
                                  <Link to="/cart">  <img
                                         src= {detail.Plink} alt='img' /></Link>
                                         <span>{detail.Price}</span>
                               <p>{detail.Description}</p>
                                    <button onClick={(detail.id)}>Add to cart</button>


                                </div>
                            </div>
                        </div>
                    )
                )}
            </div>
        );
    }
}

export default Home1;