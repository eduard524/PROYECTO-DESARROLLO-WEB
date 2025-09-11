-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 10-09-2025 a las 04:01:37
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `salon_eventos`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `clientes`
--

CREATE TABLE `clientes` (
  `id` bigint(20) NOT NULL,
  `nombres` varchar(120) NOT NULL,
  `apellidos` varchar(120) NOT NULL,
  `telefono` varchar(30) DEFAULT NULL,
  `email` varchar(160) DEFAULT NULL,
  `nit` varchar(20) DEFAULT NULL,
  `creado_en` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `comprobantes`
--

CREATE TABLE `comprobantes` (
  `id` bigint(20) NOT NULL,
  `reserva_id` bigint(20) NOT NULL,
  `tipo` enum('recibo','factura') NOT NULL DEFAULT 'recibo',
  `numero` varchar(60) NOT NULL,
  `pdf_url` varchar(255) DEFAULT NULL,
  `generado_en` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `fechas_bloqueadas`
--

CREATE TABLE `fechas_bloqueadas` (
  `id` bigint(20) NOT NULL,
  `salon_id` bigint(20) NOT NULL,
  `fecha` date NOT NULL,
  `motivo` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `imagenes_salon`
--

CREATE TABLE `imagenes_salon` (
  `id` bigint(20) NOT NULL,
  `salon_id` bigint(20) NOT NULL,
  `ruta` varchar(255) NOT NULL,
  `alt_text` varchar(200) DEFAULT NULL,
  `orden` int(11) NOT NULL DEFAULT 1,
  `creado_en` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `metodos_pago`
--

CREATE TABLE `metodos_pago` (
  `id` bigint(20) NOT NULL,
  `nombre` varchar(60) NOT NULL,
  `activo` tinyint(1) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pagos`
--

CREATE TABLE `pagos` (
  `id` bigint(20) NOT NULL,
  `reserva_id` bigint(20) NOT NULL,
  `metodo_id` bigint(20) NOT NULL,
  `monto` decimal(12,2) NOT NULL,
  `moneda` varchar(10) NOT NULL DEFAULT 'GTQ',
  `referencia_txn` varchar(120) DEFAULT NULL,
  `estado` enum('aprobado','pendiente','rechazado') NOT NULL DEFAULT 'aprobado',
  `fecha_pago` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `reservas`
--

CREATE TABLE `reservas` (
  `id` bigint(20) NOT NULL,
  `salon_id` bigint(20) NOT NULL,
  `cliente_id` bigint(20) NOT NULL,
  `fecha_evento` date NOT NULL,
  `hora_inicio` time NOT NULL,
  `hora_fin` time NOT NULL,
  `estado` enum('pendiente','confirmada','pagada','cancelada') NOT NULL DEFAULT 'pendiente',
  `total` decimal(12,2) NOT NULL DEFAULT 0.00,
  `creado_por` bigint(20) DEFAULT NULL,
  `notas` varchar(300) DEFAULT NULL,
  `creado_en` timestamp NOT NULL DEFAULT current_timestamp(),
  `actualizado_en` timestamp NULL DEFAULT NULL ON UPDATE current_timestamp()
) ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `reserva_servicio`
--

CREATE TABLE `reserva_servicio` (
  `id` bigint(20) NOT NULL,
  `reserva_id` bigint(20) NOT NULL,
  `servicio_id` bigint(20) NOT NULL,
  `cantidad` int(11) NOT NULL DEFAULT 1,
  `precio_unitario` decimal(12,2) NOT NULL,
  `subtotal` decimal(12,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `salones`
--

CREATE TABLE `salones` (
  `id` bigint(20) NOT NULL,
  `nombre` varchar(120) NOT NULL,
  `descripcion` text DEFAULT NULL,
  `direccion` varchar(200) DEFAULT NULL,
  `capacidad` int(11) DEFAULT NULL,
  `precio_base` decimal(12,2) NOT NULL DEFAULT 0.00,
  `activo` tinyint(1) NOT NULL DEFAULT 1,
  `creado_en` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `servicios`
--

CREATE TABLE `servicios` (
  `id` bigint(20) NOT NULL,
  `nombre` varchar(120) NOT NULL,
  `descripcion` text DEFAULT NULL,
  `tipo` enum('silla','mesa','sonido','adorno','combo','otro') NOT NULL DEFAULT 'otro',
  `precio_unitario` decimal(12,2) NOT NULL DEFAULT 0.00,
  `activo` tinyint(1) NOT NULL DEFAULT 1,
  `creado_en` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id` bigint(20) NOT NULL,
  `nombre` varchar(120) NOT NULL,
  `email` varchar(160) NOT NULL,
  `password_hash` varchar(200) NOT NULL,
  `rol` enum('admin','operador') NOT NULL DEFAULT 'admin',
  `activo` tinyint(1) NOT NULL DEFAULT 1,
  `creado_en` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `clientes`
--
ALTER TABLE `clientes`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indices de la tabla `comprobantes`
--
ALTER TABLE `comprobantes`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `uq_comp` (`tipo`,`numero`),
  ADD KEY `fk_comp_reserva` (`reserva_id`);

--
-- Indices de la tabla `fechas_bloqueadas`
--
ALTER TABLE `fechas_bloqueadas`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `uq_fb` (`salon_id`,`fecha`);

--
-- Indices de la tabla `imagenes_salon`
--
ALTER TABLE `imagenes_salon`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `uq_img_orden` (`salon_id`,`orden`);

--
-- Indices de la tabla `metodos_pago`
--
ALTER TABLE `metodos_pago`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `pagos`
--
ALTER TABLE `pagos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_pago_reserva` (`reserva_id`),
  ADD KEY `fk_pago_metodo` (`metodo_id`);

--
-- Indices de la tabla `reservas`
--
ALTER TABLE `reservas`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_reserva_salon` (`salon_id`),
  ADD KEY `fk_reserva_cliente` (`cliente_id`),
  ADD KEY `fk_reserva_usuario` (`creado_por`);

--
-- Indices de la tabla `reserva_servicio`
--
ALTER TABLE `reserva_servicio`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `uq_rs` (`reserva_id`,`servicio_id`),
  ADD KEY `fk_rs_servicio` (`servicio_id`);

--
-- Indices de la tabla `salones`
--
ALTER TABLE `salones`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `servicios`
--
ALTER TABLE `servicios`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `clientes`
--
ALTER TABLE `clientes`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `comprobantes`
--
ALTER TABLE `comprobantes`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `fechas_bloqueadas`
--
ALTER TABLE `fechas_bloqueadas`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `imagenes_salon`
--
ALTER TABLE `imagenes_salon`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `metodos_pago`
--
ALTER TABLE `metodos_pago`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `pagos`
--
ALTER TABLE `pagos`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `reservas`
--
ALTER TABLE `reservas`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `reserva_servicio`
--
ALTER TABLE `reserva_servicio`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `salones`
--
ALTER TABLE `salones`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `servicios`
--
ALTER TABLE `servicios`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `comprobantes`
--
ALTER TABLE `comprobantes`
  ADD CONSTRAINT `fk_comp_reserva` FOREIGN KEY (`reserva_id`) REFERENCES `reservas` (`id`) ON DELETE CASCADE;

--
-- Filtros para la tabla `fechas_bloqueadas`
--
ALTER TABLE `fechas_bloqueadas`
  ADD CONSTRAINT `fk_fb_salon` FOREIGN KEY (`salon_id`) REFERENCES `salones` (`id`);

--
-- Filtros para la tabla `imagenes_salon`
--
ALTER TABLE `imagenes_salon`
  ADD CONSTRAINT `fk_img_salon` FOREIGN KEY (`salon_id`) REFERENCES `salones` (`id`);

--
-- Filtros para la tabla `pagos`
--
ALTER TABLE `pagos`
  ADD CONSTRAINT `fk_pago_metodo` FOREIGN KEY (`metodo_id`) REFERENCES `metodos_pago` (`id`),
  ADD CONSTRAINT `fk_pago_reserva` FOREIGN KEY (`reserva_id`) REFERENCES `reservas` (`id`) ON DELETE CASCADE;

--
-- Filtros para la tabla `reservas`
--
ALTER TABLE `reservas`
  ADD CONSTRAINT `fk_reserva_cliente` FOREIGN KEY (`cliente_id`) REFERENCES `clientes` (`id`),
  ADD CONSTRAINT `fk_reserva_salon` FOREIGN KEY (`salon_id`) REFERENCES `salones` (`id`),
  ADD CONSTRAINT `fk_reserva_usuario` FOREIGN KEY (`creado_por`) REFERENCES `usuarios` (`id`);

--
-- Filtros para la tabla `reserva_servicio`
--
ALTER TABLE `reserva_servicio`
  ADD CONSTRAINT `fk_rs_reserva` FOREIGN KEY (`reserva_id`) REFERENCES `reservas` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `fk_rs_servicio` FOREIGN KEY (`servicio_id`) REFERENCES `servicios` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
