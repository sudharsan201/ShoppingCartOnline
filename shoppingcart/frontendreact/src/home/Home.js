import {Link} from 'react-router-dom';
import React  from 'react';
import axios from "axios";
import 'bootstrap/dist/css/bootstrap.css';



class Home extends React.Component {

    state = {
        details: [],
    }

    componentDidMount() {

        let data;

        axios.get("http://127.0.0.1:8000/api/products/")
        .then(res => {
                data = res.data;
                this.setState({
                    details: data,
                });
                console.log(res.data)
            })
            .catch((err) => {
            });
    }

    render() {

        return (
            
            <div id="product" className='col-lg-12' style={{justifyContent:'space-evenly',padding:'30px',margin:'auto',display:'flex',height:'350px',width:'1500px',}}>
                {this.state.details.map((detail, id) => (
             <div className='col-lg-3' style={{padding:'2px',width:'300px',height:'500px',boxShadow:'2px 2px 2px 2px darkgray',borderRadius:'20px',}}>
                 <div id="product"key={detail.id}>
                                  <strong><label style={{fontSize:'28px',fontFamily:'Arial',alignItems:'center',}}>{detail.Title} </label></strong><br/>
                                  <Link to="/cart">
                                    <img src= {detail.ImageLink} style={{maxWidth:'100%',maxHeight:'80%', borderRadius:'5px',}}/>
                                  </Link>
                                    <br/>
                                    <label style={{fontSize:'16px',fontFamily:'Times New Roman',alignItems:'center',}}>{detail.Price}</label><br/>
                                    <label style={{fontSize:'16px',fontFamily:'Times New Roman',alignItems:'center',}}>{detail.Description}</label><br/>
                                    <button onClick={(detail.id)}>Add to cart</button>
                     </div>
                 </div>
                    )
                )}
            </div>
        );
    }
}

export default Home;

