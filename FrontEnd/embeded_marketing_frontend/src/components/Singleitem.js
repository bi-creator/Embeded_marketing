import React from "react";
import './itemcss.css'

const Singlehomeitem = ({ item}) => {
    return (
        <div className="ui card product-item">
            <div className="image">
                <img src={item.thumbnail} alt={item.title}/>
            </div>
            <div className="content">
                <div className="header">{item.title}</div>
                <div className="meta">
                <span className="price">{item.extracted_price}</span>
                </div>
                <div className="description">
                    {item.product_discription}
                </div>
            </div>
            </div>
        
    )
}


export default Singlehomeitem;