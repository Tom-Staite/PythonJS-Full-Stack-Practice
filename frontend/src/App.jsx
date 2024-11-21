import { useState, useEffect } from 'react'
import './App.css'
import ContactList from './ContactList'

function App() {
  const [contacts, setContacts] = useState([])

  useEffect(() => {
    fetchContacts()
  }, [])

  const fetchContacts = async () => {
    const responce = await fetch("http://127.0.0.1:5000/contacts")
    const data = await responce.json()
    setContacts(data.contacts)
    console.log(data.contacts)

  };

  return (<><ContactList contacts={contacts}/>
  <ContactForm /></>
    
      
 
  )
};

export default App
