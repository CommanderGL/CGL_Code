let file = ''

function Edit_HTML_Button_Clicked() {
	const body = document.body
	body.innerHTML = `
	<input type="text" placeholder="File..." onkeyup="file = this.value">
	<input type="button" value="submit" onclick="window.location.href = 'html/edit/' + file" id="submit">
	`
}

function Edit_Python_Button_Clicked() {
	const body = document.body
	body.innerHTML = `
	<input type="text" placeholder="File..." onkeyup="file = this.value">
	<input type="button" value="submit" onclick="window.location.href = 'python/edit/' + file" id="submit">
	`
}

function Edit_Node_Button_Clicked() {
	const body = document.body
	body.innerHTML = `
	<input type="text" placeholder="File..." onkeyup="file = this.value">
	<input type="button" value="submit" onclick="window.location.href = 'node/edit/' + file" id="submit">
	`
}

function logout() {
	window.location.pathname = "/logout";
}