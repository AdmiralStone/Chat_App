import axios from "axios";

export default{
    login(userObj){
        let postParams = {"userObj":userObj}
        return axios.post("http://localhost:8080/login",postParams,
        {
            headers:{
                'content-type':'application/json',
            }
        })
    }
}