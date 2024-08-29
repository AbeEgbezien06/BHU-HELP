document.addEventListener('DOMContentLoaded', function() {
    fetch('/api/v1/pending')
        .then(response => response.json())
        .then(data => {
            const complaintsList = document.getElementById('complaintsList');
            data.forEach(complaint => {
                const listItem = document.createElement('li');
                listItem.textContent = `${complaint.name} - ${complaint.hostel}`;
                complaintsList.appendChild(listItem);
            });
            console.log(data)
        })
        .catch(error => console.error('Error fetching complaints:', error));
});
