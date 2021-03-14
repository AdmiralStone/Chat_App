import LoginService from '@/services/loginService.js';

export const namespaced = true;

export const state ={
    userObj:null
}
/******************************************************/
/******************************************************/
export const mutations ={
    SET_USER(state,userObj){
        state.userObj = userObj
    }
}
/******************************************************/
/******************************************************/
export const actions= {
    userLogin({commit},currentForm){
        return LoginService.login(currentForm).then(res => {
            if(res.data.status !== undefined && res.data.status !== null && res.data.status === 'success'){
                let userObj = res.data.userObj;
                commit('SET_USER',userObj);
            }else{
                throw (res.data.message)
            }
        })
        .catch(error =>{
            throw error;
        })
    }
}
/******************************************************/
/******************************************************/