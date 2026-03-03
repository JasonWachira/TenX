import { useRouter } from "@tanstack/react-router"
const menu = [
    { name: "Home", path: "/" },
    { name: "About", path: "/about" },
    { name: "Candidates", path: "/candidates" },
]

function NavigationTop(){
    const router = useRouter()
    return (
        <div className="w-full p-12 flex justify-between items-center ">
            <h1>Welcome to the Finance Watch</h1>
            <div className="flex items-center">
            {menu.map((item) => (
                <a key={item.path} href={item.path} className={`px-4 py-2 transition-all duration-150 ${router.state.location.pathname === item.path ? 'bg-[var(--muted-foreground)] text-white' : ''}`}>
                    {item.name}
                </a>
            ))}
            </div>

        </div>
    )
}


function NavigationBottom(){
    return (
        <div className="bottom-0 p-12 fixed">
            
        </div>
)}

export { 
    NavigationTop,
    NavigationBottom
}