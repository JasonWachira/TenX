import { Outlet, createRootRoute } from '@tanstack/react-router'
import { useQueryClient, QueryClientProvider, QueryClient } from '@tanstack/react-query'
import { TanStackRouterDevtoolsPanel } from '@tanstack/react-router-devtools'
import { TanStackDevtools } from '@tanstack/react-devtools'
import {NavigationTop, NavigationBottom} from '../components/navigation'
import '../styles.css'

const queryClient = new QueryClient()


export const Route = createRootRoute({
  component: RootComponent,
})

function RootComponent() {
  return (
    <QueryClientProvider client={queryClient}>
      <NavigationTop />
      <Outlet />
      <TanStackDevtools
        config={{
          position: 'bottom-right',
        }}
        plugins={[
          {
            name: 'TanStack Router',
            render: <TanStackRouterDevtoolsPanel />,
          },
        ]}
      />
      <NavigationBottom />
    </QueryClientProvider>
  )
}
