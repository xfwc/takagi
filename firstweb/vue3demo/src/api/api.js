import axios from 'axios'
let base = 'http://127.0.0.1:5000'

export const requestLogin = params => {
    let result
    return axios({
        method: 'POST',
        url: `${base}/login`,
        data: params
    })
    //     .then(res => {
    //         result = res.data
    //     console.log(result)
    //     console.log(typeof result)})
    return result
}

export const requestRegister = params => {
    let result
    return axios({
        method: 'POST',
        url: `${base}/register`,
        data: params
    })
    return result
}