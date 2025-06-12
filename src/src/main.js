import { mount } from 'svelte'
import './app.css'
// Mount the homepage component
import Homepage from './Homepage.svelte'

const app = mount(Homepage, {
  target: document.getElementById('app'),
})

export default app
