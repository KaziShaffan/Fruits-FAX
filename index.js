let confirm = async () => {
  let name = document.getElementById("name").value;
  try {
    let response = await fetch(`http://localhost:6969/api/${name}`);
    let fruit = await response.json();

    console.log(fruit);

    nutritionformatted = nutritionsformat(fruit.nutritions);

    fruitHTML = `
    <div class="innerBox">
      <h3>${fruit.name}</h3>
      <div>${nutritionformatted}</div>
    </div>
    `;

    document.getElementById("display").innerHTML = fruitHTML;
  } catch (error) {
    alert("PROBLEMS BRUV");
    console.error("ERROR COULD NOT FETCH FRUIT:", error);
  }
};

let nutritionsformat = (nutrition) => {
  let nutritionHTML = "<ul>";

  for (let key in nutrition) {
    nutritionHTML += `<li>${key}: ${nutrition[key]}</li>`;
  }
  nutritionHTML += "</ul>";

  return nutritionHTML;
};
