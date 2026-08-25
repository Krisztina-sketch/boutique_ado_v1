document.addEventListener("DOMContentLoaded", function () {
    const deleteForms = document.querySelectorAll(".delete-product-form");

    deleteForms.forEach(function (form) {
        form.addEventListener("submit", function (event) {
            const confirmed = confirm(
                "Are you sure you want to delete this product?"
            );

            if (!confirmed) {
                event.preventDefault();
            }
        });
    });
});