/** @type {import('next').NextConfig} */
const nextConfig = {
    async rewrites() {
        return [
            {
            source: '/chat',
            destination: 'http://api:10000/chat',
            },
        ];
        },
};

export default nextConfig;
