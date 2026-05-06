import NavBar from '../Header_Footer/NavBar.jsx';
import Footer from '../Header_Footer/Footer.jsx';
import Form from 'react-bootstrap/Form';
import React from 'react'
import { useState } from "react";
import  '../styling/main.css';
export default function Main() {
const [message,setmessage] = useState([]);
const [input,setInput] = useState("");
const[url,setUrl] = useState("")
const [sessionId] = useState(()=> Math.random().toString(36).substring(2))
const [loading,setLoading] = useState(false);

const sendmessage = async()=>{
    if(!input){
      return
    }
    const newmessage = [...message,{type:"user",text:input}];
    setmessage(newmessage);
    setLoading(true);

    try{
      const res = await fetch("http://127.0.0.1:8000/getAnswer",{
        method : "Post",
        headers:{
          "Content-Type":"application/json"
        },
        body:JSON.stringify({
          url:url,
          query : input,
          session_id : sessionId
        })
      });
      const data = await res.json();
      setmessage([...newmessage,{type: "bot", text: data.answer}])
    }catch(error){
      setmessage([...newmessage, {type:"bot",text:"error connecting to server"}])
    }

    

    setLoading(false);
    
    setInput("");
};

  return (
    <div>
        <NavBar />
        <div className='container-fluid text-start mt-5'>
            <label htmlFor="urlInput">paste yout URL here</label>
            <div className='col-lg-7 col-12 col-md-8 '>
          <input id='urlInput' type='text' className='form-control  border border-dark ' placeholder='paste your valid youtube URL' value={url} onChange={(e)=>setUrl(e.target.value)}></input>
          </div>


    <div className='container-fluid border mt-4' style={{height:"400px", overflowY:"auto"}}>
      {message.map((msg,index)=>{
        return(
          
              <div key={index} className={`mb-2 d-flex ${msg.type === "user" ? "justify-content-end" : "justify-content-start"}`}>

                    <div className={`p-2 rounded ${msg.type === "user"? "bg-primary text-white":"bg-primary text-white"}`} 
                    style={{maxWidth:"70%", width:"fit-content",wordWrap:"break-word",whiteSpace:"pre-wrap"}}>
                        {msg.text}
                    </div>
                     
              </div>
              
     ) })}    
      {loading &&(
                      <div className='d-flex justify-content-start'>
                        <div className='p-2 bg-warning rounded '>
                          Ruko jra Sabar kro <span className='dots fs-3 fw-bold'></span>
                        </div>

                      </div>
                    )}                                              
    </div>

              <div className='d-flex mt-4 '>
                <textarea type="text" className='form-control' value={input} onChange={(e)=> setInput(e.target.value)}
                placeholder='type your message' rows={1}   style={{ resize: "none" }}
                onKeyDown={(e)=>e.key ==="Enter" && sendmessage()} />
                <button onClick={sendmessage} className='btn btn-success ms-2'>send</button>
              </div>
              

    </div>
    <Footer />
    </div>
  )
}

