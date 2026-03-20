document.addEventListener('DOMContentLoaded', () => {
    console.log("зайшов в js")
    FilePond.registerPlugin(FilePondPluginImagePreview);

    const inputElement = document.querySelector('#product-images');

    const uploadUrl = inputElement.dataset.uploadUrl;
    const deleteUrl = inputElement.dataset.deleteUrl;
    const csrfToken = inputElement.dataset.csrfToken;

    const pond = FilePond.create(inputElement, {
        allowMultiple: true,
        allowReorder: true,
        allowImagePreview: true,
        imagePreviewHeight: 150,
        server: {
            process: {
                // url: "{% url 'products:upload_temp_image' %}",
                url: uploadUrl,
                method: 'POST',
                headers: {
                    // 'X-CSRFToken': '{{ csrf_token }}'
                    'X-CSRFToken': csrfToken
                },
                onload: (response) => JSON.parse(response).file_id,
                onerror: (response) => console.log("Error:", response)
            },
            revert: (uniqueFileId, load, error) => {
                fetch(deleteUrl, {
                    method: 'DELETE',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': '{{ csrf_token }}'
                    },
                    body: JSON.stringify({ file_id: uniqueFileId })
                })
                .then(res => res.json())
                .then(res => {
                    if(res.status === "ok") load();
                    else error(res.error || "Error deleting file");
                })
                .catch(err => error("Error deleting file"));
            }
        }
    });

    const form = document.querySelector('#product-form');
    form.addEventListener('submit', function() {
        form.querySelectorAll('input[name="images"]').forEach(el => el.remove());

        pond.getFiles().forEach((file, index) => {
            const input = document.createElement('input');
            input.type = 'hidden';
            input.name = 'images';
            input.value = file.serverId;
            input.dataset.priority = index;
            form.appendChild(input);
        });
    });
});