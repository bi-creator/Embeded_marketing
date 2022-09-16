import React,{ useState} from "react";
import Searchbar from "./Searchbar";
import Api from "./Api";
import Singlehomeitem from "./Singleitem";
const App=()=>{
    const [result,setresult]=useState([])
    const rendreditems=result.map((item)=>{
        return(
          <Singlehomeitem item={item} />
        )
    })
    const itemsubmit=async(item,formData)=>{
        const responce= await Api.post('/data',formData,{params:{productname:item

        }});
        // console.log(item,image)
    
        if(!responce){
            return null
        }
        setresult(responce.data)
        console.log(result)
        
    }

    return(
        <div className="ui container">
            <Searchbar onItemsubmit={itemsubmit}/>
            <div className="ui four cards">{rendreditems}</div>
        </div>
    )
}

export default App;