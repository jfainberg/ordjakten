function $(q) {
    return document.querySelector(q);
}

async function top1k(secret) {
    const url = "/nearby_1k/" + btoa(secret);
    const response = await fetch(url);
    if (response.status != 200) {
        return null;
    }
    try {
        return response.text();
    } catch (e) {
        return null;
    }
}

function init() {
        $('#form').addEventListener('submit', async function(event) {
            event.preventDefault();
            const word = $('#word').value.trim().replace("!", "").replace("*", "");
            $("#top1k").innerHTML = "";
            const nearby = await top1k(word);
            if (nearby == null) {
                $('#response').innerHTML = `Unknown secret word ${word}.`;
                return;
            }
            let nearby_inside = nearby.replace(/.*<body>/s, "");
            nearby_inside = nearby_inside.replace(/<\/body>.*/s, "");
            $("#top1k").innerHTML = nearby_inside;
            $("#nearest").style.display = "block";

            const len = word.length;
            const digits = 20 - len;
            const randomDigits1 = (Math.random() * 10000000000).toFixed(0);
            const randomDigits2 = (Math.random() * 10000000000).toFixed(0);
            const randomDigits = (randomDigits1 + randomDigits2);
            const urlSecret = word + randomDigits.substring(0, digits);;
            const url = `https://semantle.novalis.org/?word=${btoa(urlSecret)}`;
            $('#response').innerHTML = `<a href="${url}">${url}</a>`;

        });
}

window.addEventListener('load', async () => { init() });
