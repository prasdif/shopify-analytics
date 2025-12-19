import React from 'react';
import ChatInterface from './components/ChatInterface';
import { LayoutDashboard, ShoppingBag, Users, BarChart3, Settings } from 'lucide-react';

function App() {
  return (
    <div className="flex h-screen bg-background text-white selection:bg-primary/30">

      {/* Sidebar */}
      <aside className="w-64 bg-surface border-r border-white/5 flex flex-col hidden md:flex">
        <div className="p-6 border-b border-white/5">
          <div className="flex items-center gap-3">
            <div className="w-8 h-8 rounded-lg bg-gradient-to-br from-primary to-emerald-600 flex items-center justify-center font-bold text-white">
              S
            </div>
            <span className="font-bold text-lg tracking-tight">ShopifyAI</span>
          </div>
        </div>

        <nav className="flex-1 p-4 space-y-2">
          <NavItem icon={<LayoutDashboard size={20} />} label="Dashboard" active />
          <NavItem icon={<ShoppingBag size={20} />} label="Products" />
          <NavItem icon={<Users size={20} />} label="Customers" />
          <NavItem icon={<BarChart3 size={20} />} label="Analytics" />
          <div className="pt-4 mt-4 border-t border-white/5">
            <NavItem icon={<Settings size={20} />} label="Settings" />
          </div>
        </nav>

        <div className="p-4 border-t border-white/5">
          <div className="bg-white/5 rounded-xl p-4 flex items-center gap-3">
            <div className="w-8 h-8 rounded-full bg-accent flex items-center justify-center text-sm font-bold">
              JD
            </div>
            <div className="flex-1 min-w-0">
              <p className="text-sm font-medium truncate">Demo Store</p>
              <p className="text-xs text-gray-500 truncate">admin@shop.com</p>
            </div>
          </div>
        </div>
      </aside>

      {/* Main Content */}
      <main className="flex-1 flex flex-col h-full overflow-hidden relative">
        {/* Top Gradient */}
        <div className="absolute top-0 left-0 w-full h-96 bg-primary/5 rounded-full blur-[120px] -translate-y-1/2 pointer-events-none" />

        <div className="p-4 md:p-8 flex-1 overflow-hidden flex flex-col">
          <header className="mb-8 z-10">
            <h1 className="text-3xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-white to-gray-400">
              Insights & AI Assistant
            </h1>
            <p className="text-gray-400 mt-2">
              Ask deep questions about your inventory, sales velocity, and customer trends.
            </p>
          </header>

          <div className="flex-1 overflow-hidden z-10">
            <ChatInterface />
          </div>
        </div>
      </main>
    </div>
  );
}

function NavItem({ icon, label, active = false }) {
  return (
    <button className={`w-full flex items-center gap-3 px-4 py-3 rounded-xl text-sm font-medium transition-all ${active
        ? 'bg-primary text-white shadow-lg shadow-primary/20'
        : 'text-gray-400 hover:bg-white/5 hover:text-white'
      }`}>
      {icon}
      {label}
    </button>
  );
}

export default App;
