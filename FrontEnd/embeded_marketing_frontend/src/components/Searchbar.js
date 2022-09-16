import React,{useState} from "react";
const Searchbar=({onItemsubmit})=>{
   
    const [item,setitem]=useState('')
    const [image,setimage]=useState(null)
  
    const Oninputchange=(evnet)=>{
        setitem(evnet.target.value)
    }
    const Onimagechange=(event)=>{
        setimage(event.target.files[0])
    }
    const onUpload=(event)=>{
        const formData = new FormData();
    
      // Update the formData object
      formData.append(
        'file',
        image,
        image.name
      )
      event.preventDefault();
      onItemsubmit(item,formData);
    }
    // const OnFormSubmit=(event)=>{
    //     event.preventDefault();
    //     onItemsubmit(item,image);
    // }
      
    return(
        <div className="ui segment search-bar ">
            <form  className="ui form">
            <div className="field">
                <label>Enter Product Name</label>
                <input type='text' value={item} onChange={Oninputchange} />
                <label>Upload image related to product</label>
                <input onChange={Onimagechange} type='file' name="image"/>
                <button onClick={onUpload}>Upload</button>
            </div>
        </form>
        </div>
    )
}


export default Searchbar;