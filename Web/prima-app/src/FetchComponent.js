import React, { useState } from "react";


const FetchComponent = () => {
    const url = 'https://jsonplaceholder.typicode.com/users';
    const [users, setUsers]=useState([]);
    return (

        <div>
            {

                users.map((u)=>{
                    return <p key={u.id}>{u.name}</p>
                })
            }
        </div>
    )
};

export default FetchComponent;