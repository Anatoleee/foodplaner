import "./App.css"
import {useEffect, useState} from "react";

export default function Main(){

    const [json, setJson] = useState(null);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await fetch('http://127.0.0.1:8080/api');
                const result = await response.json();
                console.log(result);
                setJson(result);
            } catch (error) {
                console.error('Error fetching data:', error);
            }
        };
        fetchData();
    }, []);

    const restart = async () => {
        try {
            fetch("http://127.0.0.1:8080/restart")
            window.location.reload(false)
        } catch (error) {
            console.log(error)
        }
    };

    return (
        <div className="wrapper">
            <div className="body">
                <h1 className="title">FoodPlaner 🍔</h1>
                <div className="menu">
                    <table>
                        <thead>
                            <tr>
                                <th></th>
                                <th>Midi</th>
                                <th>Soir</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td className="day">Lundi</td>
                                <td>{json?.day?.lundi}</td>
                                <td>{json?.night?.lundi}</td>
                            </tr>
                            <tr>
                                <td className="day">Mardi</td>
                                <td>{json?.day?.mardi}</td>
                                <td>{json?.night?.mardi}</td>
                            </tr>
                            <tr>
                                <td className="day">Mercredi</td>
                                <td>{json?.day?.mercredi}</td>
                                <td>{json?.night?.mercredi}</td>
                            </tr>
                            <tr>
                                <td className="day">Jeudi</td>
                                <td>{json?.day?.jeudi}</td>
                                <td>{json?.night?.jeudi}</td>
                            </tr>
                            <tr>
                                <td className="day">Vendredi</td>
                                <td>{json?.day?.vendredi}</td>
                                <td>{json?.night?.vendredi}</td>
                            </tr>
                            <tr>
                                <td className="day">Samedi</td>
                                <td>{json?.day?.samedi}</td>
                                <td>{json?.night?.samedi}</td>
                            </tr>
                            <tr>
                                <td className="day">Dimanche</td>
                                <td>{json?.day?.dimanche}</td>
                                <td>{json?.night?.dimanche}</td>
                            </tr>
                        </tbody>
                    </table>
                    <button onClick={restart}>Générer un nouveau repas</button>
                </div>
                <p className="credit">Anatole CAPELLE 2024 ｜<a href="https://github.com/Anatoleee" className="credit_link"> github.com/Anatoleee </a></p>
            </div>
        </div>
    );
}