document.addEventListener("DOMContentLoaded",function(){
    document.getElementById("recepie_button").addEventListener("click", get_recepies);
    document.getElementById("benefit_button").addEventListener("click", get_benefits);
})




MAIN_URL = "http://127.0.0.1:5000/"

let add_detail = (list, id_name, h2_name) => {
    console.log(list)
    let div = document.getElementById(`${id_name}`)
    div.innerHTML = `<h2>${h2_name}</h2>`
    let all_list = document.createElement("ul")
    for(let element of list){
        let li = document.createElement("li")
        li.innerText = `${element}`
        all_list.appendChild(li)
    }
    div.appendChild(all_list)

}

let fetch_single = async (endpoint_name, fetch_name) => {
    all_data = []
    await fetch(`${MAIN_URL}${endpoint_name}/${fetch_name}`)
    .then((response) => response.json())
    .then((data) => all_data = data)
    return all_data
}

let handle_button = async (endpoint_name, btn_name, name_first_detail, name_second_details) => {
    let fetched_data = await fetch_single(endpoint_name, btn_name)
    if (fetched_data['benefits'] !== undefined){
        add_detail(fetched_data.benefits, "first-detail", name_first_detail)
        add_detail(fetched_data.ingredients, "second-detail", name_second_details)
    }
    else{
        add_detail(fetched_data.recipes, "first-detail", name_first_detail)
    }
    
}

let add_handlers_to_buttons = (fetch_name ,btn_list, name_first_detail, name_second_details) =>{
    for(let btn of btn_list){
        btn.addEventListener('click', () => {
            handle_button(fetch_name, btn.name, name_first_detail, name_second_details)
        })
    }
}

let create_buttons = (fetched_list) => {
    let buttons = [];
    for(let item of fetched_list){
        let recipe_name = item.name
        let element_ul = document.createElement("ul")
        let element_button = document.createElement("button")
        element_button.setAttribute('class', "btn btn-warning")
        element_button.setAttribute('name', recipe_name)
        element_button.innerText = recipe_name
        element_ul.appendChild(element_button)
        buttons.push(element_button)
        document.getElementById("first_list").appendChild(element_ul)
    }
    return buttons
}

let clear = () => {
    // clear h2
    for(let h2 of document.querySelectorAll('h2')){
        h2.innerText = ''
    }
    //clear first detail
    document.getElementById('first-detail').innerText = ''
    //clear second detail
    document.getElementById('second-detail').innerText = ''
}

let get_recepies = async () =>{
    clear()
    const main_div = document.getElementById("first_list").innerHTML = '';
    let fetched_recipes = await fetch_data('recepies');
    let buttons = create_buttons(fetched_recipes);
    add_handlers_to_buttons("recepies", buttons, "Benefits", "Ingredients");
};


let get_benefits = async () =>{
    clear()
    const main_div = document.getElementById("first_list").innerHTML = '';
    let fetched_recipes = await fetch_data('benefits');
    let buttons = create_buttons(fetched_recipes);
    add_handlers_to_buttons("benefits", buttons, "Receipes", "Ingredients");
}

let fetch_data = async (fetch_name) => {
    all_data = []
    await fetch(`${MAIN_URL}${fetch_name}`)
    .then((response) => response.json())
    .then((data) => all_data = data)
    return all_data
}


