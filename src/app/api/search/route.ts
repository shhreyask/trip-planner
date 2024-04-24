import axios from "axios"

export async function POST(request: Request) {
    let place = request.body
    const apiKey = process.env.TOMTOM
    const endpoint = `https://api.tomtom.com/search/2/search/${place}.json?extendedPostalCodesFor=Geo&minFuzzyLevel=1&maxFuzzyLevel=2&view=IN&relatedPois=off&key=${apiKey}`
    const res = await axios.get(endpoint)
    console.log(res.data.results[0].position)
    return Response.json(res.data.results[0].position) 
}
