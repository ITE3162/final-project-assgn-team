let titleInput = document.querySelector("input[name=title]"); // or ("id_title")
let slugInput = document.querySelector("input[name=slug]"); // or ("id_slug")

let slugfy = (title)=>{
     return title.toString().toLowerCase().trim()
     .replace(/&/g, "-and-")
     .replace(/[\s\W-]+/g, "-")
}

titleInput.addEventListener('input', (e)=>{ // or listen to 'keyup'
   return slugInput.setAttribute("value", slugfy(titleInput.value))
})