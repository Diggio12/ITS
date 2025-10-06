const API_URL = "http://localhost:3000/tasks";

export const fetchTasks = async () => {
    const response = await fetch(API_URL);
    if (!response.ok) throw new Error("Errore fetch");
    const data = await response.json();
    return data;
};


export const addTaskService = async (text) => {
    await fetch(API_URL, {
        method: "POST",
        heades: {"Content-Type" : "application/json"},
        body: JSON.stringify({text, completed: false}),
    })

};



export const deleteService = async (id) =>{
    await fetch(API_URL+"/"+id,{method : "DELETE"});

};