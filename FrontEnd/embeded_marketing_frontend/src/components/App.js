import React,{ useEffect, useState} from "react";
// import Searchbar from "./Searchbar";
import Api from "./Api";
import Singlehomeitem from "./Singleitem";
// import { useSearchParams } from "react-router-dom";
const App=()=>{
    const [result,setresult]=useState([])
    // const [getPrams]=useSearchParams()
    // const itemName=getPrams.get('itemName')
    const getPrams = new URLSearchParams(window.location.search)
    const rendreditems=result.map((item)=>{
        return(
          <Singlehomeitem item={item} />
        )
    })
    useEffect(()=>{
    const itemsubmit=async()=>{
        console.log()
        const responce= await Api.post(`/data?productname=${getPrams.get('itemName')}`)
        // console.log(item,image)
    
        if(!responce){
            return null
        }
        setresult(responce.data)
        console.log(result)
        
    }
    itemsubmit();
    
},[])

    return(
        <div className="ui container">
            {/* <Searchbar onItemsubmit={itemsubmit}/> */}
            <div className="ui four cards">{rendreditems}</div>
        </div>
    )
}

export default App;