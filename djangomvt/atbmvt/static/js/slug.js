const nameInput = document.getElementById("name");
const slugInput = document.getElementById("slug");
const toggle = document.getElementById("auto-slug");

function transliterate(text) {
    const map = {
        'а':'a','б':'b','в':'v','г':'h','ґ':'g','д':'d','е':'e','є':'ye',
        'ж':'zh','з':'z','и':'y','і':'i','ї':'yi','й':'y','к':'k','л':'l',
        'м':'m','н':'n','о':'o','п':'p','р':'r','с':'s','т':'t','у':'u',
        'ф':'f','х':'kh','ц':'ts','ч':'ch','ш':'sh','щ':'shch','ю':'yu','я':'ya'
    };

    return text
        .toLowerCase()
        .split('')
        .map(char => map[char] || char)
        .join('')
        .replace(/[^a-z0-9]+/g, '-')
        .replace(/^-+|-+$/g, '');
}

document.addEventListener("DOMContentLoaded", function() {

    nameInput.addEventListener("input", function() {
        if (toggle.checked) {
            slugInput.value = transliterate(this.value);
            slugInput.readOnly = true
        } else {
            slugInput.readOnly = false;
        }
    });
});