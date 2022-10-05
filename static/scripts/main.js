
document.addEventListener('DOMContentLoaded', () => {

    // Create useful variables
    const table = document.querySelector('#display_results');
    table.style.borderCollapse = 'collapse';
    const headers = ['Search Title', 'Associated Web Site'];
    let tableRow = document.createElement('tr');
    let allRows = [];
    let index = -1;

    //connect socket to a server
    let socket = io.connect('http://127.0.0.1:5000/')
    
    //Initiate search for data
    document.querySelector('#perform_search').onclick = () => {

        // Parsing the search value into acceptable google format
        let originalSearch = document.querySelector('#search').value;
        let finalSearchTem = originalSearch.replace(' ', '+');

        //Sending search value to our server
        socket.send(finalSearchTem);
        console.log(finalSearchTem);

        
        // We'll store data in a table
        // After initiating search display table headers
        const main = document.getElementById('search_bar');
        main.remove()
        for (let i = 0; i < headers.length; i++) {
            let tableHeader = document.createElement('th');
            tableHeader.setAttribute('id', `${i}`);
            let headerText = document.createTextNode(headers[i]);
            tableHeader.style.fontFamily = 'Josefin Sans, sans-serif';
            tableHeader.appendChild(headerText);
            tableRow.appendChild(tableHeader);
            tableHeader.style.marginBottom = '50px';
        }
    
        table.appendChild(tableRow);

    }

    // Wehn socket receives data from server...
    // ...we create necessary HTML elements and display searched data as table data in table rows
    socket.on('message', data => {

        let all_data = data.split('+');
        let tr = document.createElement('tr');
        tr.classList.add('created-rows')
        allRows.push(tr);
        let td1 = document.createElement('td');
        let td2 = document.createElement('td');
        let dataText1 = document.createTextNode(all_data[0]);
        let dataText2 = document.createTextNode(all_data[1]);

        td1.style.fontFamily = 'Josefin Sans, sans-serif';
        td2.style.fontFamily = 'Josefin Sans, sans-serif';

        td1.appendChild(dataText1);
        td2.appendChild(dataText2);
        td1.style.borderBottom = '1px solid black';
        td2.style.borderBottom = '1px solid black';
        tr.appendChild(td1);
        tr.appendChild(td2);
        table.appendChild(tr);

        index ++;

        // display even rows of our table in different color than odd rows for a more visually pleasing look
        if (index % 2 === 0 ) {
            console.log(allRows[index])
            allRows[index].style.backgroundColor = '#f0fef6';
        } else {
            allRows[index].style.backgroundColor = 'white';
        }

    });

});


