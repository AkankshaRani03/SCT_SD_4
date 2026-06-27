/* ============================================
   ProductVision AI
   script.js
============================================ */

const themeBtn =
document.getElementById("themeToggle");

/* -------------------------------
   Theme Toggle
--------------------------------*/

if(localStorage.getItem("theme") === "light"){

    document.body.classList.add("light-mode");

    if(themeBtn){
        themeBtn.innerHTML = "☀";
    }

}

if(themeBtn){

    themeBtn.addEventListener("click",()=>{

        document.body.classList.toggle(
            "light-mode"
        );

        if(
            document.body.classList.contains(
                "light-mode"
            )
        ){

            localStorage.setItem(
                "theme",
                "light"
            );

            themeBtn.innerHTML="☀";

        }

        else{

            localStorage.setItem(
                "theme",
                "dark"
            );

            themeBtn.innerHTML="🌙";

        }

    });

}

/* -------------------------------
   Search Loading Animation
--------------------------------*/

const form =
document.querySelector("form");

if(form){

    form.addEventListener(
        "submit",
        ()=>{

            const btn =
            form.querySelector("button");

            btn.innerHTML =
            "⏳ Searching...";

            btn.disabled = true;

        }
    );

}

/* -------------------------------
   Animate Statistics
--------------------------------*/

function animateValue(element){

    if(!element) return;

    const target =
    Number(
        element.innerText
    );

    if(isNaN(target)) return;

    let value = 0;

    const speed =
    Math.max(
        5,
        Math.floor(
            target/40
        )
    );

    const timer =
    setInterval(()=>{

        value += speed;

        if(value >= target){

            value = target;

            clearInterval(timer);

        }

        element.innerHTML=value;

    },25);

}

document.querySelectorAll(
".stat-box h3"
).forEach(card=>{

    animateValue(card);

});

/* -------------------------------
   Table Search Filter
--------------------------------*/

const searchBox =
document.querySelector(
'input[name="keyword"]'
);

const rows =
document.querySelectorAll(
"tbody tr"
);

if(searchBox){

    searchBox.addEventListener(
        "keyup",
        ()=>{

            const value =
            searchBox.value.toLowerCase();

            rows.forEach(row=>{

                row.style.display=

                row.innerText
                .toLowerCase()
                .includes(value)

                ? ""

                : "none";

            });

        }
    );

}

/* -------------------------------
   Row Hover Effect
--------------------------------*/

rows.forEach(row=>{

    row.addEventListener(
        "mouseenter",
        ()=>{

            row.style.transition=".3s";

        }
    );

});

/* -------------------------------
   Image Preview
--------------------------------*/

document
.querySelectorAll("tbody img")
.forEach(img=>{

    img.title=
    "Product Preview";

});

/* -------------------------------
   Product Counter
--------------------------------*/

const totalProducts =
document.querySelector(
".stat-box h3"
);

if(totalProducts){

    console.log(

        "Products Found :",

        totalProducts.innerText

    );

}

/* -------------------------------
   Export Notification
--------------------------------*/

document
.querySelectorAll("a button")
.forEach(btn=>{

    btn.addEventListener(
        "click",
        ()=>{

            setTimeout(()=>{

                alert(

                "Download Started Successfully!"

                );

            },300);

        }
    );

});

/* -------------------------------
   Smooth Scroll
--------------------------------*/

window.scrollTo({

    top:0,

    behavior:"smooth"

});

console.log(
"ProductVision AI Loaded Successfully"
);