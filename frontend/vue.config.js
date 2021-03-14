module.exports = {
    devServer: {
        proxy: {
            '/login':{
                target:'http://localhost:5000/',
            },
            '/ws':{
                target:'http://localhost:5000/',
                ws:false
            }
        }
}

}