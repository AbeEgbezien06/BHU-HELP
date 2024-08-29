document.addEventListener('DOMContentLoaded', function() {
    var hostelField = document.getElementById('id_hostel');
    var blockField = document.getElementById('id_block').closest('.form-row');

    function toggleBlockField() {
        if (hostelField.value === 'OBH' || hostelField.value === 'OGH') {
            blockField.style.display = '';
        } else {
            blockField.style.display = 'none';
        }
    }

    toggleBlockField(); // Initial call to set the correct display
    hostelField.addEventListener('change', toggleBlockField);
});
