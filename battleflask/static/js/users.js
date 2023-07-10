const user_list = document.querySelector(".users");
const ref = document.querySelector(".refresh");
const submit_user = document.querySelector(".submit_user");
const message_list = document.querySelector(".messages");



const display_users = async () => {
	const response = await fetch("http://192.168.0.26:5000/users");

	const array = await response.json();

	users = array.users;
	console.log(array.users)
	user_list.innerHTML = '';

	users.forEach(u => {
		var anchor = document.createElement('a');
		var linkText = document.createTextNode(u);
		anchor.appendChild(linkText)
		console.log(anchor)
		anchor.href = "http://192.168.0.26/"+u+"/invite";
		var li = document.createElement("li");
		li.appendChild(anchor);
		li.classList.add("list-group-item")

		user_list.appendChild(li)
	});
	user_list.firstElementChild.setAttribute("aria-current", "true");
}

const display_messages = async () => {
	const response = await fetch("http://192.168.0.26:5000/messages");

	const array = await response.json();

	messages = array.messages;
	console.log(array.messages)
	message_list.innerHTML = '';

	console.log(messages)
	messages.forEach(m => {	
		var li = document.createElement("li");
		li.innerHTML = m;
		li.classList.add("list-group-item")

		user_list.appendChild(li)
	});
	message_list.firstElementChild.setAttribute("aria-current", "true");
}
/*
const addUserButton = async () => {
	add.addEventListener("click", () => {
		let x = document.forms["formUser"]["username"].value;
		let error = document.querySelector(".error");
		if(x == ""){
			error.innerHTML = "Name must be filled out"
		}
		else {
			addUser().then((data) => {
			})
		}
	})
}

const addUser = () => {
	const response = await fetch("http://192.168.0.26/new_user", {
		method: "POST",
		mode: "cors",
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify(data);
	})
	return response.json();
	
}*/

/*setInterval(() => {
	display_users()
}, 10000);*/

display_users();


display_messages();
//addUser();
