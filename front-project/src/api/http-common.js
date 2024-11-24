import axios from "axios";

export default axios.create({
  baseURL: "http://127.0.0.1:5000/" || process.env.VUE_APP_API_URL ,
  headers: {
    "Content-type": "application/json"
  }
});