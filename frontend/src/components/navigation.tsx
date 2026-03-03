import { useRouter } from "@tanstack/react-router"



const menu = [
    { name: "Home", path: "/" },
    { name: "About", path: "/about" },
    {name:"Candidates", path: "/candidates"},
]


function NavigationTop() {
    const router = useRouter()
    return (
        <nav className="navbar mb-6 flex justify-between navbar-expand-lg navbar-light bg-light">
            <h1>Welcome to the TenX Hackathon Project</h1>

            <div className="flex items-center gap-4">
            {menu.map((item) => (
                <a key={item.path} className={`nav-link transition-all hover:bg-gray-200 p-2 duration-150 ${item.path === router.state.location.pathname ? 'bg-gray-300' : ''}`} href={item.path}>
                    {item.name}
                </a>
            ))}
            </div>
        </nav>
    )
}



function NavigationBottom() {
    return (
        <footer className="bottom-0 fixed">
       
        </footer>
    )
}


export { NavigationTop, NavigationBottom }